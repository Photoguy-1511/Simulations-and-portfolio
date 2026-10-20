# Earthquake Building Vibration Simulation

A simple structural dynamics simulation built in **Simulink** exploring how a building responds to an external earthquake-like force, and how **structural damping** affects its motion.

## Overview

This project investigates a fundamental structural engineering question:

> **How does damping affect the motion of a building subjected to an external disturbance?**

The building is simplified as a **mass–spring–damper system**. The mass represents the building itself, the spring represents the building's structural stiffness, and the damper represents mechanisms that dissipate vibration energy.

Two simulations are compared:

* **Undamped:** structural stiffness is present, but no damping is applied.
* **Damped:** the same structure is given a damping coefficient of 500 Ns/m.

The same external input is applied to both systems so that the effect of damping can be isolated.

---

## Engineering Model

The building is represented using the standard mass–spring–damper equation:

$$
m\ddot{x}+c\dot{x}+kx=F(t)
$$

where:

* **m** = Building mass (kg)
* **c** = Damping coefficient (Ns/m)
* **k** = Structural stiffness (N/m)
* **x** = Building displacement (m)
* **ẋ** = Building velocity (m/s)
* **ẍ** = Building acceleration (m/s²)
* **F(t)** = External earthquake-like force (N)

The Simulink model calculates the net force:

$$
F_{net}=F(t)-c\dot{x}-kx
$$

Acceleration is then obtained from:

$$
\ddot{x}=\frac{F_{net}}{m}
$$

Two integrators convert:

$$
\ddot{x}\rightarrow\dot{x}\rightarrow x
$$

allowing the final building displacement to be observed.

---

## Physical Interpretation

The components of the Simulink model represent physical behaviour:

* **Mass:** Represents the inertia of the building.
* **Spring:** Represents the **structural stiffness** of the building. It is not intended to represent a literal coil spring.
* **Damper:** Represents mechanisms that dissipate vibrational energy.
* **Integrator 1:** Converts acceleration into velocity.
* **Integrator 2:** Converts velocity into displacement.
* **Scope:** Displays the resulting building displacement.

The spring stores energy and produces a restoring force when the building is displaced:

$$
F_{spring}=-kx
$$

The damper removes energy from the system according to:

$$
F_{damping}=-c\dot{x}
$$

---

## Simulation Parameters

The same physical parameters are used for both simulations:

* Building mass: **1,000 kg**
* Structural stiffness: **1,000 N/m**
* External force amplitude: **1,000 N**
* External force frequency: **3 rad/s**
* Simulation time: **20 s**

### Undamped Case

* Damping coefficient: **0 Ns/m**

### Damped Case

* Damping coefficient: **500 Ns/m**

Only the damping coefficient is changed between the two cases.

---

## Simulink Architecture

The model follows this structure:

$$
F(t)
\rightarrow
\text{Net Force}
\rightarrow
\frac{1}{m}
\rightarrow
\int
\rightarrow
\int
\rightarrow
x(t)
$$

Feedback paths provide the restoring and damping forces:

* Displacement → Spring → negative feedback
* Velocity → Damper → negative feedback

This creates a closed physical system in which the building's current motion affects the forces acting on it.

---

## Results

### Undamped System

With:

$$
c=0
$$

the building continues to oscillate because there is no mechanism for removing energy from the system.

The displacement therefore remains significant throughout the simulation.

### Damped System

With:

$$
c=500\ \text{Ns/m}
$$

the damper dissipates vibrational energy.

The resulting displacement has a noticeably smaller response compared with the undamped system.

---

## Engineering Interpretation

The simulation demonstrates that **structural stiffness alone does not remove vibrational energy**.

An undamped structure can continue oscillating when subjected to repeated external excitation. Introducing damping reduces the energy stored in the vibration and therefore reduces the resulting structural motion.

This highlights why damping is an important consideration when designing structures subjected to dynamic loads such as earthquakes.

---

## Limitations

This is a simplified educational model rather than a complete earthquake-structure simulation.

* The building is represented as a single degree-of-freedom system.
* The earthquake input is represented by a sinusoidal external force rather than recorded ground-motion data.
* The building is assumed to have constant mass, stiffness, and damping.
* Nonlinear structural behaviour is not included.
* Real buildings contain multiple floors and vibration modes.

The model is therefore intended to demonstrate the **fundamental effect of stiffness and damping on structural vibration**, rather than predict the behaviour of a specific real building.