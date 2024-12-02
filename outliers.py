Q1 = data['A'].quantile(0.25)
Q3 = data['A'].quantile(0.75)
IQR = Q3 - Q1
data_filtered = data[~((data['A'] < (Q1 - 1.5 * IQR)) | (data['A'] > (Q3 + 1.5 * IQR)))]
print(data_filtered)
