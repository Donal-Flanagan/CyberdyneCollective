from .create_word_value import get_keywords_and_values, get_lemitized_words_in_order, create_words_and_values,save_words_and_values
from .compare_word_with_corpus import get_all_txt_files_in_directory,compare_single_file,compare_file_list,get_sorted_key_words,get_top_values, evaluate_corpus, get_overall_values_only
import nltk
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")