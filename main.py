# Imports
from tokenize import String
import pandas as pd

# Reading TSV Data using Pandas and Removing Duplicate Data
def read_somatic_mutation_data(inputFile):
    return pd.read_csv(inputFile,sep='\t') \
            .drop_duplicates(subset=['icgc_mutation_id']);

# Q1
# Finding Patterns for Allele Mutations using GroupBy
def mutated_Patterns(inputFile):
    somatic_mutation_data = read_somatic_mutation_data(inputFile);
    return somatic_mutation_data[["icgc_mutation_id","mutated_from_allele","mutated_to_allele"]] \
            .groupby(["mutated_from_allele", "mutated_to_allele"])["icgc_mutation_id"] \
            .count() \
            .reset_index(name='Counts of unique_icgc_mutation_id')

# Q2
# min_max_icgc_sample = somatic_mutation_data[["icgc_mutation_id","icgc_sample_id"]].groupby(["icgc_sample_id"])["icgc_mutation_id"].count().sort_values(ascending=False)
# min_max_icgc_sample = somatic_mutation_data[["icgc_mutation_id","icgc_sample_id"]].groupby(["icgc_sample_id"])["icgc_mutation_id"].count().nlargest(2)

# Finding Min & Max for icgc_sample
def min_max_icgc_sample(inputFile, reqOutput):
    somatic_mutation_data = read_somatic_mutation_data(inputFile);
    if reqOutput is not None:
        if reqOutput == "min":
            return somatic_mutation_data[["icgc_mutation_id","icgc_sample_id"]].groupby(["icgc_sample_id"])["icgc_mutation_id"].count().idxmin()
        if reqOutput == "max":
            return somatic_mutation_data[["icgc_mutation_id","icgc_sample_id"]].groupby(["icgc_sample_id"])["icgc_mutation_id"].count().idxmax()
    
def main():
    inputFile = "simple_somatic_mutation.open.BLCA-CN.tsv";
    # Q1: Returns Mutated Patterns
    mutated_Patterns_data = mutated_Patterns(inputFile)
    print(mutated_Patterns_data)
    #Q2: Finding Min & Max for icgc_sample
    min_icgc_sample = min_max_icgc_sample(inputFile, "min") # min
    max_icgc_sample = min_max_icgc_sample(inputFile, "max") #max
    print(min_icgc_sample)
    print(max_icgc_sample)  



if __name__ == "__main__":
    main()

# Test case: Create dummy data, check if each function returns correct data.
# Check for Null Values, Empty data, data validation



