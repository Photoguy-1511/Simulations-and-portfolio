# Cessna Caravan Wing Bending Stress Analysis

A simple structural engineering simulation built in **MATLAB** exploring how aerodynamic loading produces bending moment and bending stress along the wing of a **Cessna 208 Caravan**.

## Overview

This project investigates a fundamental aircraft structural question:

> **How does aerodynamic lift produce bending stress along an aircraft wing?**

The wing is simplified as a **cantilever beam**, fixed at the wing root and free at the wing tip. The aircraft is assumed to be flying in steady, level cruise, allowing the total lift to be approximated by the aircraft weight.

The project then distributes this lift uniformly across the wing and calculates the resulting bending moment and bending stress from the wing root to the wing tip.

---

## Engineering Background

For steady, level flight:

$$
L = W
$$

where:

* **L** = Total lift (N)
* **W** = Aircraft weight (N)

The lift is divided equally between the two wings. For one wing, the lift is treated as a uniformly distributed load:

$$
w = \frac{L/2}{b/2}
$$

where:

* **w** = Distributed wing load (N/m)
* **b** = Total wingspan (m)

The bending moment along one wing is calculated using the uniformly distributed load:

$$
M(x) = \frac{w(L-x)^2}{2}
$$

Bending stress is then calculated using the beam bending equation:

$$
\sigma = \frac{Mc}{I}
$$

where:

* **σ** = Bending stress (Pa)
* **M** = Bending moment (N·m)
* **c** = Distance from the neutral axis to the outer surface (m)
* **I** = Second moment of area (m⁴)

For the assumed rectangular structural cross-section:

$$
I = \frac{ch^3}{12}
$$

---

## Aircraft and Flight Conditions

The simulation uses representative cruise conditions for a **Cessna 208 Caravan**:

* Altitude: **2,500 m**
* Cruise speed: **90 m/s**
* Aircraft mass: **3,000 kg**
* Wing area: **25.96 m²**
* Wingspan: **15.88 m**

The aircraft mass is assumed to represent a typical mid-cruise condition rather than maximum takeoff weight.

Atmospheric temperature, pressure, and density are calcu
