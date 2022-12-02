from TestOrchestrator4ML_main.label_perturbation_attack.knn import euc_dist, predict, calculate_k, calculate_metrics, perform_interference

if __name__ == "__main__":
    inputs = [69, "sedan", 52, 0, "football", {"dictionary":"definition"}, 42]

    for x in inputs:
        try:
            euc_dist(x, "four")
        except Exception as e:
            print(e)

    for x in inputs:
        try:
            predict(x, 422)
        except Exception as e:
            print(e)

    for x in inputs:
        try:
            calculate_k(x, "first", 7, "last")
        except Exception as e:
            print(e)

    for x in inputs:
        try:
            calculate_metrics(x, 104, "choom")
        except Exception as e:
            print(e)

    for x in inputs:
        try:
            perform_interference(x, "y", "z", 1, 2)
        except Exception as e:
            print(e)