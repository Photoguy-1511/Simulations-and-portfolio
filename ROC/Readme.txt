# Effect of Aircraft Weight on Climb Performance

A simple engineering simulation built in **MATLAB** exploring how aircraft weight influences climb performance using the steady-state rate of climb equation.

## Overview

This project investigates a fundamental question in aircraft performance:

> **How does aircraft weight affect the maximum achievable rate of climb, assuming all other variables remain constant?**

Rather than building a highly detailed aircraft model, this project isolates **weight** as the only changing parameter. This allows the effect of weight on climb performance to be studied independently before introducing more complex aerodynamic effects.

---

## Engineering Background

The model uses the steady-state climb equation:

[
ROC = \frac{(T-D)V}{W}
]

where:

* **ROC** = Rate of Climb (m/s)
* **T** = Thrust (N)
* **D** = Drag (N)
* **V** = Climb Speed (m/s)
* **W** = Aircraft Weight (N)

Since thrust, drag, and climb speed are held constant, the equation predicts an inverse relationship between aircraft weight and climb performance.

---

## Assumptions

To isolate the effect of weight, the following assumptions were made:

* Constant engine thrust
* Constant aerodynamic drag
* Constant climb speed
* Steady-state climb
* Standard atmospheric conditions
* Aircraft modeled using approximate performance values for a **Cessna 172 Skyhawk**
* Weight changes only between observations and is not continuously updated during the climb calculation

These assumptions intentionally simplify the physics so that only the influence of aircraft weight is examined.

---

## Methodology

1. Define representative performance values for a Cessna 172.
2. Estimate aircraft weight reduction from fuel consumption during a **3-hour cruise** using:

   * Average fuel burn rate
   * Standard Avgas density
3. Calculate the corresponding minimum aircraft weight.
4. Generate ten evenly spaced weight values between minimum and maximum weight.
5. Compute the rate of climb for each weight using the steady-state climb equation.
6. Plot:

   * Aircraft weight versus flight time (illustrating assumed fuel burn)
   * Rate of climb versus aircraft weight

---

## Results

The simulation demonstrates the expected trend:

* As aircraft weight increases, the available rate of climb decreases.
* Lower aircraft weight produces a higher climb rate because the same excess thrust is required to lift less weight.
* The relationship is nonlinear due to weight appearing in the denominator of the governing equation.

Although simplified, the model reproduces the qualitative behavior observed in real aircraft performance.

---

## Limitations

This project intentionally omits several real-world effects, including:

* Variation of thrust with altitude
* Drag changes with lift coefficient and airspeed
* Fuel burn during the climb itself
* Propeller efficiency changes
* Atmospheric density variation
* Engine power degradation with altitude

These simplifications make the project suitable as a first-principles parameter study rather than a complete flight performance simulation.

---

## Future Improvements

Planned extensions include:

* Incorporating altitude-dependent air density using the ISA atmosphere model
* Modeling drag as a function of lift coefficient
* Updating aircraft weight continuously as fuel burns
* Including engine power variation with altitude
* Comparing simulated climb performance with published Cessna 172 performance charts
* Building an interactive MATLAB App Designer interface for parameter exploration

---

## Skills Demonstrated

* MATLAB programming
* Engineering parameter studies
* Aircraft performance fundamentals
* Mathematical modeling
* Data visualization
* Engineering assumptions and model validation

---

## Project Status

Completed as an introductory MATLAB engineering simulation.

This project is part of a larger portfolio documenting my progression in computational engineering using **MATLAB**, **Simulink**, and **ANSYS**, with each project introducing progressively more realistic engineering models.
