import json
import os
import re
import tensorflow as tf
def label_processing(folder):
    train_dict = {}
    test_dict = {}
    valid_dict = {}
    for file in os.listdir(folder):
        with open(file, "r", encoding='utf-8') as f:
            data = json.load(f)
        train_labels = data["ground_truth"]["train"]
        test_labels = data["ground_truth"]["test"]
        valid_labels = data["ground_truth"]["valid"]
        train_dict = clean_texts(train_labels, train_dict)
        test_dict = clean_texts(test_labels, test_dict)
        valid_dict = clean_texts(valid_labels, valid_dict)

    return train_dict, test_dict, valid_dict
def clean_texts(data, dict):
    for img_filename, image_data in data.items():
        text = image_data["text"]
        allowed_chars = r"[^A-Za-zÀ-ÖØ-öø-ÿ0-9.,:;!?()\"'&*\-\s\n]"
        clean_text = re.sub(allowed_chars, " ", text)
        clean_text = re.sub(r"[ ]{2,}", " ", clean_text).strip()
        dict[img_filename] = clean_text
    return dict
