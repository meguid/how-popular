data = load('trainingEthnicity.txt');
X = data(:, 1);
y = data(:, 2);
m = length(y); % number of training examples
plot(X, y, 'rx', 'MarkerSize', 10); % Plot the data
ylabel('Popularity Rate 0 - 100'); % Set the y−axis label
xlabel('Ethnicity'); % Set the x−axis labe
set (gca, 'xtick', [0 1 2 3 4 5 6 7])
set (gca, 'xticklabel', [" ";"Asian"; "Asian/Indian";"Black";"Middle Eastern";"Multiracial";"White";"OTHER"])
get (gca, 'xticklabelmode')
xlim([0 8])
title ("Plotting relationship values between ethnicity and popularity");
