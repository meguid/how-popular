data = load('trainingWaistTop.txt');
X = data(:, 1);
y = data(:, 2);
m = length(y); % number of training examples
plot(X, y, 'rx', 'MarkerSize', 10); % Plot the data
ylabel('Popularity Rate 0 - 100'); % Set the y−axis label
xlabel('Waist Size in inches'); % Set the x−axis labe
xlim([min(X)-1 max(X)+1])
title ("Plotting relationship values between waist size and popularity (Top 200 Celebrity Data)");
