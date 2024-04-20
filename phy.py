import streamlit as st

# Function to calculate Wavefunction probability density
def wavefunction_probability_density(psi):
    return abs(psi)**2

# Function to calculate Maximum kinetic energy (Photoelectric equation)
def photoelectric_equation(h, f, phi):
    return h * f + phi

# Function to calculate Hydrogen atom spectrum
def hydrogen_atom_spectrum(R, ni, nf):
    return 1 / (R * (1 / ni**2 - 1 / nf**2))

# Function to calculate Dipole moment potential
def dipole_moment_potential(mu, B, z):
    return -mu * B * z

# Streamlit app
def main():
    st.title("Quantum Mechanics Formulas Calculator")

    formula_options = {
        "Wavefunction probability density": wavefunction_probability_density,
        "Photoelectric equation": photoelectric_equation,
        "Hydrogen atom spectrum": hydrogen_atom_spectrum,
        "Dipole moment potential": dipole_moment_potential
    }

    selected_formula = st.selectbox("Select a formula:", list(formula_options.keys()))

    if selected_formula:
        inputs = {}

        if selected_formula == "Wavefunction probability density":
            inputs['psi'] = st.number_input("Enter wavefunction (Psi):", step=0.1)
        elif selected_formula == "Photoelectric equation":
            inputs['h'] = st.number_input("Enter Planck's constant (h):", step=0.1)
            inputs['f'] = st.number_input("Enter frequency of light (f):", step=0.1)
            inputs['phi'] = st.number_input("Enter work function (Phi):", step=0.1)
        elif selected_formula == "Hydrogen atom spectrum":
            inputs['R'] = st.number_input("Enter Rydberg constant (R):", step=0.1)
            inputs['ni'] = st.number_input("Enter initial energy level (ni):", step=1)
            inputs['nf'] = st.number_input("Enter final energy level (nf):", step=1)
        elif selected_formula == "Dipole moment potential":
            inputs['mu'] = st.number_input("Enter dipole moment (mu):", step=0.1)
            inputs['B'] = st.number_input("Enter magnetic field strength (B):", step=0.1)
            inputs['z'] = st.number_input("Enter orientation factor (z):", step=0.1)

        if st.button("Calculate"):
            result = formula_options[selected_formula](**inputs)
            st.success(f"Result: {result}")

if __name__ == "__main__":
    main()
