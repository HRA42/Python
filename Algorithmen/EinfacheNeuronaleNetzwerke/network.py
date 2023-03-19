from __future__ import annotations
from typing import List, Callable, TypeVar, Tuple
from functools import reduce
from layer import Layer
from util import sigmoid, derivative_sigmoid

T = TypeVar('T')  # Ausgabetyp der Interpretation des neuronalen Netzwerks


class Network:
    def __init__(self, layer_structure: List[int], learning_rate: float,
                 activation_function: Callable[[float], float] = sigmoid,
                 derivative_activation_function: Callable[[float], float] = derivative_sigmoid) -> None:
        if len(layer_structure) < 3:
            raise ValueError("Fehler: Es sollte mindestens 3 Schichten geben (1 Eingabe, 1 versteckte, 1 Ausgabe)")
        self.layers: List[Layer] = []
        # Eingabeschicht
        input_layer: Layer = Layer(None, layer_structure[0], learning_rate, activation_function,
                                   derivative_activation_function)
        self.layers.append(input_layer)
        # Versteckte Schichten und Ausgabeschicht
        for previous, num_neurons in enumerate(layer_structure[1::]):
            next_layer = Layer(self.layers[previous], num_neurons, learning_rate, activation_function,
                               derivative_activation_function)
            self.layers.append(next_layer)

    # Schiebt Eingabedaten in die erste Schicht, dann die Ausgabe der ersten
    # als Eingabe in die zweite, von der zweiten in die dritte usw.
    def outputs(self, input: List[float]) -> List[float]:
        return reduce(lambda inputs, layer: layer.outputs(inputs), self.layers, input)

    # Die Änderungen jedes Neurons anhand der Fehler in der Ausgabe
    # im Vergleich zum erwarteten Ergebnis ermitteln
    def backpropagate(self, expected: List[float]) -> None:
        # Delta für Neuronen der Ausgabeschicht berechnen
        last_layer: int = len(self.layers) - 1
        self.layers[last_layer].calculate_deltas_for_output_layer(expected)
        # Delta für versteckte Schichten in umgekehrter Reihenfolge berechnen
        for l in range(last_layer - 1, 0, -1):
            self.layers[l].calculate_deltas_for_hidden_layer(self.layers[l + 1])

    # backpropagate() verändert selbst keine Gewichte
    # diese Funktion verwendet die in backpropagate() berechneten Deltas,
    # um tatsächlich Änderungen an den Gewichten auszuführen
    def update_weights(self) -> None:
        for layer in self.layers[1:]:  # Eingabeschicht überspringen
            for neuron in layer.neurons:
                for w in range(len(neuron.weights)):
                    neuron.weights[w] = neuron.weights[w] + (
                            neuron.learning_rate * (layer.previous_layer.output_cache[w]) * neuron.delta)

    # train() verwendet die Ergebnisse von outputs(), die mit mehreren Eingaben ausgeführt
    # und mit expected verglichen werden, um backpropagate() und update_weights() zu füttern
    def train(self, inputs: List[List[float]], expected: List[List[float]]) -> None:
        for location, xs in enumerate(inputs):
            ys: List[float] = expected[location]
            outs: List[float] = self.outputs(xs)
            self.backpropagate(ys)
            self.update_weights()

    # Für verallgemeinerte Ergebnisse, die Klassifikation benötigen, gibt diese Funktion die Anzahl
    # der korrekten Versuche und den prozentualen Anteil der korrekten Versuche an der Gesamtzahl zurück
    def validate(self, inputs: List[List[float]], expected: List[T], interpret_output: Callable[[List[float]], T]) -> \
            Tuple[int, int, float]:
        correct: int = 0
        for input, expected in zip(inputs, expected):
            result: T = interpret_output(self.outputs(input))
            if result == expected:
                correct += 1
        percentage: float = correct / len(inputs)
        return correct, len(inputs), percentage
