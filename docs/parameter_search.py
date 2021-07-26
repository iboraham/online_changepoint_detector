import roerich


def parameter_search_rulsif(search_space, X, eval_metric, annotations):
    current_param_set = {}
    for param_name in search_space.keys():
        current_param_set.update({param_name: search_space[param_name][0]})

    set_list = []
    res = {}
    for param_name in search_space.keys():
        for param in search_space[param_name]:
            current_param_set.update({param_name: param})
            if len(set(current_param_set)) == len(current_param_set):
                set_list.append(current_param_set)
                cpd = roerich.OnlineNNRuLSIF(
                    search_space,
                )
                _, preds = cpd.predict(X)
                measure = eval_metric(annotations, preds)
                res.update({current_param_set: measure})
    return res
