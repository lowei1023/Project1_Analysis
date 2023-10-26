import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



class EDA:
    def __init__(self, df):
        self.df = df
    """
    Parameters:

    df: The input DataFrame that will be used for analysis and visualization.

    """
   
    
    def generate_summary_statistics(self):
        return self.df.describe()
    """
    Parameters: 
    None (uses the DataFrame self.df initialized in the constructor)
    
    Returns:  
    The method returns a summary statistics DataFrame generated using the describe() function applied to the input DataFrame.
    
    """


    def generate_histograms(self):
        plt.figure(figsize=(12, 8))
        plt.subplots_adjust(hspace=0.5)

   
        for i, column in enumerate(self.df.columns[1:]):
            plt.subplot(3, 2, i + 1)
            plt.hist(self.df[column], bins=20, color='skyblue', edgecolor='black')
            plt.title(column)
            plt.xlabel(column)
            plt.ylabel('Frequency')

        plt.show()
        
        plt.figure(figsize=(12, 8))
        plt.subplots_adjust(hspace=0.5)
        
        for i, column in enumerate(self.df.columns[1:]):
            plt.subplot(3, 2, i + 1)
            sns.histplot(self.df[column], bins=20, kde=True, color='skyblue')
            plt.title(column)
            plt.xlabel(column)
            plt.ylabel('Density')

        plt.show()

        """
        Parameters:
        None: This method does not take any additional parameters. It utilizes the DataFrame (self.df) that was passed during the object instantiation.
        
        Returns:
        None: This method doesn't return any value. It generates and displays histograms for each column in the DataFrame using Matplotlib and Seaborn libraries. The histograms are displayed but not returned as a value.
        
        """

