def remove_small_classes(text_data, class_data, class_size_threshold):
    all_classes = list(set(class_data))
    all_classes.sort()
    classcounts = {cl: len([x for x in class_data
                            if x == cl]) for cl in all_classes}

    # We remove classes that are too small -----------------------------
    goodclasses = set([cl for cl, count in classcounts.items()
                       if count > class_size_threshold])

    good_indices = [i for i in range(len(text_data))
                    if class_data[i] in goodclasses]

    text_data = [text_data[i] for i in good_indices]
    class_data = [class_data[i] for i in good_indices]

    return text_data, class_data