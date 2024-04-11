import matplotlib.pyplot as plt

def plot_histogram():
    # Write Q1 code here
    sat_scores = []
    gpa_scores = []
    with open("admission_algorithms_dataset.csv", 'r') as of:
        of.readline()
        for line in of:
            line_list = line.split(',')
            sat_scores.append(float(line_list[1]))
            gpa_scores.append(float(line_list[2]))
    #Plotting Sat Histogram
    plt.hist(sat_scores)
    plt.savefig("sat_score.png")
    plt.clf()

    #Plotting GPA Scores
    plt.hist(gpa_scores)
    plt.savefig("gpa.png")
    plt.clf()


def plot_scatter():
    sat_scores = []
    gpa_scores = []
    with open("admission_algorithms_dataset.csv", 'r') as of:
        of.readline()
        for line in of:
            line_list = line.split(',')
            sat_scores.append(float(line_list[1]))
            gpa_scores.append(float(line_list[2]))
    plt.scatter(gpa_scores, sat_scores)
    plt.savefig('correlation.png')
    plt.clf()

def plot_spectra():
    wavelengths_1 = []
    flux_1 = []
    with open("spectrum1.txt", 'r') as of:
        for line in of:
            line_list = line.split()
            wavelengths_1.append(float(line_list[0]))
            flux_1.append(float(line_list[1]))
    plt.plot(wavelengths_1, flux_1, 'blue')

    wavelengths_2 = []
    flux_2 = []
    with open("spectrum2.txt", 'r') as of:
        for line in of:
            line_list = line.split()
            wavelengths_2.append(float(line_list[0]))
            flux_2.append(float(line_list[1]))
    plt.plot(wavelengths_2, flux_2, 'green')
    plt.savefig('spectra.png')
    plt.clf()

def main():
    plot_histogram()
    plot_scatter()
    plot_spectra()
    pass


if __name__ == "__main__":
    main()
