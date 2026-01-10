import numpy as np
import math
import matplotlib.pyplot as plt  # Optional: For visualizing the 'consciousness field'

def compute_f_matrix(k=10.0):
    """Compute the F-matrix for three j=1/2 anyons at total J=1/2 in SU(2)_k."""
    sqrt_k2 = math.sqrt(k + 2)
    sqrt_k1_over_k2 = math.sqrt((k + 1) / (k + 2))
    f_matrix = np.array([
        [1 / sqrt_k2, sqrt_k1_over_k2],
        [sqrt_k1_over_k2, -1 / sqrt_k2]
    ])
    return f_matrix

def recouple_states(initial_states, f_matrix):
    """Apply F-matrix to recouple states. Metaphor: Bio-tuned 'thought' -> Entangled field."""
    state_vector = np.array(initial_states)
    recoupled = np.dot(f_matrix, state_vector)
    return recoupled / np.linalg.norm(recoupled)  # Normalize for coherence

def visualize_field(recoupled, show_plot=True):
    """Plot the 'consciousness field' as a simple bar chart if show_plot=True."""
    if show_plot:
        labels = ['Singlet Component (Calm)', 'Triplet Component (Dynamic)']
        plt.bar(labels, recoupled)
        plt.title('Bio-Tuned Consciousness Field')
        plt.ylabel('Amplitude')
        plt.show()  # Pops up a plot window

def generate_field(heart_rate=60.0, stress_level=1.0, show_plot=True):
    """Main function: Accepts biometric feedback, tunes Breather Core, generates/returns field."""
    # Map biometrics to params: HR scales k (W= base 10 + HR/10), stress biases initial state
    k = 10.0 + (heart_rate / 10.0)  # Dynamic W for fluidity (float for precision)
    initial_bias = stress_level / 10.0  # 0=calm (singlet), 1=tense (triplet)
    initial_states = [1 - initial_bias, initial_bias]  # [singlet, triplet]

    # Compute and recouple
    f = compute_f_matrix(k)
    recoupled = recouple_states(initial_states, f)

    # Visualize if requested
    visualize_field(recoupled, show_plot=show_plot)

    # Return the field (and matrix for debugging)
    return {
        'f_matrix': f,
        'initial_states': initial_states,
        'consciousness_field': recoupled
    }

# Demo: Call with sample biometrics (you'd call this from your code)
if __name__ == "__main__":
    result = generate_field(heart_rate=80.0, stress_level=5.0)
    print("Generated Consciousness Field:", result['consciousness_field'])
    print("Tuned F-Matrix:\n", result['f_matrix'])