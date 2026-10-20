% Project: Effect of Aircraft Weight on Climb Performance
% Date: 23/07/2026
% Author: Shaurya Raman
% Description: Simple parameter study using the steady-state climb
% equation ROC = (Thrust - Drag) * V / Weight
% Assumptions: Constant thrust, Constant drag, Constant climb speed
% All assumptions are estimated for a Cessna 172 Sky-hawk
% Thrust, drag, and vertical speed are assumed to be independent of weight
% to isolate the effect of weight on rate of climb

thrust = 2000;             % N
drag = 950;                % N
climb_speed = 39;          % m/s
max_weight = 10900;        % N
observations = 10;

% Estimate minimum weight using fuel burn over a cruise period of 3 hrs
% Assumption: constant fuel burn rate (ignores burn variation with power setting/altitude)
% Used to derive a realistic min_weight
% not to simulate weight changing over time in the ROC model itself

fuel_burn_rate = 8.5;      % gallons per hour (average cruise burn)
fuel_density   = 6;        % lb per gallon of standard avgas
lb_to_N        = 4.448;    % conversion 
flight_time    = 3;        % hours

weight_loss_lb = fuel_burn_rate * fuel_density * flight_time;
weight_loss_N  = weight_loss_lb * lb_to_N;

min_weight = max_weight - weight_loss_N;

weight = linspace(min_weight, max_weight, observations);
time = linspace(3,0,10);
plot (time,weight, "w-o");
xlabel("Time (hrs)");
ylabel("Weight (N)");

ROC = ((thrust - drag)*climb_speed)./weight;

plot(weight, ROC, "g-o");
xlabel("Weight (N)");
ylabel("Rate Of Climb (m/s)");