clear ; close all; clc

data = load('trainingBust.txt');
X = data(:, 1);
y = data(:, 3);
m = length(y); % number of training examples
plot(X, y, 'rx', 'MarkerSize', 10); % Plot the data
ylabel('Popularity Rate 0 - 100'); % Set the y−axis label
xlabel('Bust Size in inches'); % Set the x−axis labe
title ("Plotting relationship values between bust size and popularity");


X = [ones(m, 1), data(:,1), data(:,2)]; % Add a column of ones to x
%X = [ones(m, 1), data(:,1)]; % Add a column of ones to x

%theta = zeros(3, 1); % initialize fitting parameters
% Some gradient descent settings
%iterations = 15000;
%alpha = 0.0001;
%theta = gradientDescent(X, y, theta, alpha, iterations)
hold on; % keep previous plot visible
theta = [0.000000000001;0.0107435187; -0.0398300781e-02]
plot(data(:, 1), X*theta, '-')
X*theta;
