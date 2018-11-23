# ECG-analysis-BiomedicalEngineering-
Pb1.py is a python code that takes Data1.txt which containes ECG signal amplitudes and samples it with sampling rate 512Hz.
Then you can plot the ECG signal using matplotlib library, applying some filtration after that to get R signals.
I applied differentiation, squaring the derivative, smoothing the squared signal with a moving average window of size 31 samples.
then we apply autocorrelation formula and plot lags on the x-axis with the autocorrelation values on the y-axis, I also implemented a function that prints out average heart rate from the plot of autocorrelation too.
