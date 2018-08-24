data = load('trainingCupTop.txt');
X = data(:, 1);
y = data(:, 2);
m = length(y); % number of training examples
plot(X, y, 'rx', 'MarkerSize', 10); % Plot the data
ylabel('Popularity Rate 0 - 100'); % Set the y−axis label
xlabel('Cup Sizes'); % Set the x−axis labe
xlim([min(X)-1 max(X)+1])
title ("Top 200 Celebrity Data");
set (gca, 'xtick', [0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22])
set (gca, 'xticklabel', [" ";"A";"AA";"B";"C";"D";"DD";"DDD";"E";"EE";"EEE";"F";"FF";"FFF";"G";"GG";"GGG";"H";"HH";"J";"K";"L"])
get (gca, 'xticklabelmode')
title ("Plotting relationship values between Cup size and popularity (Top 200 Celebrity Data)");
