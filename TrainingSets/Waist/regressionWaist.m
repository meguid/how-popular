data = load('trainingWaist.txt');
X = data(:, 1);
y = data(:, 2);
m = length(y); % number of training examples
plot(X, y, 'rx', 'MarkerSize', 10); % Plot the data
ylabel('Popularity Rate 0 - 100'); % Set the y−axis label
xlabel('Waist Size in inches'); % Set the x−axis labe
xlim([0 100])
title ("Plotting relationship values between waist size and popularity");
