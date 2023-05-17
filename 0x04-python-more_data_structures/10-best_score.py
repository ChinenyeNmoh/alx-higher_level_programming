#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        sorted_items = sorted(a_dictionary.items(), key=lambda item: item[1], reverse=True)
        for key, value in sorted_items:
            return key
