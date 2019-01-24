import warnings
warnings.simplefilter('error', UserWarning)
print('Before')
warnings.warn('Write your warning message here')
print('After')

