import pandas as pd
import pickle
import numpy as np


def group_features_no_rts(df):
    y = df['label']
    # Drop unwanted columns
    df = df.drop(['label'], axis=1)

    user_features = df[["followers_count", "followees_count",
                        "followers_to_friends", "tweets_count", "listed_count", "favorites_count", "default_profile",
                        "default_profile_image", "verified", "location", "url", "description", "name_length",
                        "screen_name_length", "description_length", "numerics_in_name_count",
                        "numerics_in_screen_name_count", "hashtags_in_name", "hashtags_in_description",
                        "urls_in_description", "bot_word_in_name", "bot_word_in_screen_name", "bot_word_in_description",
                        "tweet_posting_rate_per_day", "favorite_rate_per_day", "name_screen_name_similarity",
                        "description_sentiment", "description_emojis"]]

    temporal_features = df[["min_tweets_per_day", "max_tweets_per_day", "mean_tweets_per_day", "median_tweets_per_day",
                            "std_tweets_per_day", "skew_tweets_per_day", "kurt_tweets_per_day",
                            "entropy_tweets_per_day",
                            "min_tweets_per_hour", "max_tweets_per_hour", "mean_tweets_per_hour",
                            "median_tweets_per_hour", "std_tweets_per_hour", "skew_tweets_per_hour",
                            "kurt_tweets_per_hour", "entropy_tweets_per_hour", "consecutive_days_of_no_activity",
                            "consecutive_days_of_activity", "consecutive_hours_of_no_activity",
                            "consecutive_hours_of_activity", "min_avg_time_between_tweets",
                            "max_avg_time_between_tweets", "mean_avg_time_between_tweets",
                            "median_avg_time_between_tweets", "std_avg_time_between_tweets",
                            "skew_avg_time_between_tweets", "kurt_avg_time_between_tweets",
                            "entropy_avg_time_between_tweets", "max_occurence_of_same_gap_in_seconds"]]

    content_features = df[["min_text_size",
                           "max_text_size",
                           "mean_text_size",
                           "median_text_size",
                           "std_text_size",
                           "skew_text_size",
                           "kurt_text_size",
                           "entropy_text_size",
                           "min_text_entropy",
                           "max_text_entropy",
                           "mean_text_entropy",
                           "median_text_entropy",
                           "std_text_entropy",
                           "skew_text_entropy",
                           "kurt_text_entropy",
                           "entropy_text_entropy",
                           "min_similarity",
                           "max_similarity",
                           "mean_similarity",
                           "median_similarity",
                           "std_similarity",
                           "skew_similarity",
                           "kurt_similarity",
                           "entropy_similarity",
                           "NN_proportion",
                           "VB_proportion",
                           "RB_proportion",
                           "WP_proportion",
                           "WDT_proportion",
                           "DT_proportion",
                           "JJ_proportion",
                           "PRP_proportion",
                           "UH_proportion",
                           "min_NN",
                           "max_NN",
                           "mean_NN",
                           "median_NN",
                           "std_NN",
                           "skew_NN",
                           "kurt_NN",
                           "entropy_NN",
                           "min_VB",
                           "max_VB",
                           "mean_VB",
                           "median_VB",
                           "std_VB",
                           "skew_VB",
                           "kurt_VB",
                           "entropy_VB",
                           "min_RB",
                           "max_RB",
                           "mean_RB",
                           "median_RB",
                           "std_RB",
                           "skew_RB",
                           "kurt_RB",
                           "entropy_RB",
                           "min_WP",
                           "max_WP",
                           "mean_WP",
                           "median_WP",
                           "std_WP",
                           "skew_WP",
                           "kurt_WP",
                           "entropy_WP",
                           "min_DT",
                           "max_DT",
                           "mean_DT",
                           "median_DT",
                           "std_DT",
                           "skew_DT",
                           "kurt_DT",
                           "entropy_DT",
                           "min_WDT",
                           "max_WDT",
                           "mean_WDT",
                           "median_WDT",
                           "std_WDT",
                           "skew_WDT",
                           "kurt_WDT",
                           "entropy_WDT",
                           "min_JJ",
                           "max_JJ",
                           "mean_JJ",
                           "median_JJ",
                           "std_JJ",
                           "skew_JJ",
                           "kurt_JJ",
                           "entropy_JJ",
                           "min_PRP",
                           "max_PRP",
                           "mean_PRP",
                           "median_PRP",
                           "std_PRP",
                           "skew_PRP",
                           "kurt_PRP",
                           "entropy_PRP",
                           "min_UH",
                           "max_UH",
                           "mean_UH",
                           "median_UH",
                           "std_UH",
                           "skew_UH",
                           "kurt_UH",
                           "entropy_UH",
                           "min_marks",
                           "max_marks",
                           "mean_marks",
                           "median_marks",
                           "std_marks",
                           "skew_marks",
                           "kurt_marks",
                           "entropy_marks",
                           "tweet_retweet_ratio",
                           "min_tags",
                           "max_tags",
                           "mean_tags",
                           "median_tags",
                           "std_tags",
                           "skew_tags",
                           "kurt_tags",
                           "entropy_tags",
                           "min_urls",
                           "max_urls",
                           "mean_urls",
                           "median_urls",
                           "std_urls",
                           "skew_urls",
                           "kurt_urls",
                           "entropy_urls",
                           "min_mentions",
                           "max_mentions",
                           "mean_mentions",
                           "median_mentions",
                           "std_mentions",
                           "skew_mentions",
                           "kurt_mentions",
                           "entropy_mentions",
                           "min_symbols",
                           "max_symbols",
                           "mean_symbols",
                           "median_symbols",
                           "std_symbols",
                           "skew_symbols",
                           "kurt_symbols",
                           "entropy_symbols",
                           "min_media",
                           "max_media",
                           "mean_media",
                           "median_media",
                           "std_media",
                           "skew_media",
                           "kurt_media",
                           "entropy_media",
                           "source_change",
                           "source_types",
                           "unique_mentions_rate",
                           "min_favs",
                           "max_favs",
                           "mean_favs",
                           "median_favs",
                           "std_favs",
                           "skew_favs",
                           "kurt_favs",
                           "entropy_favs",
                           "min_rts",
                           "max_rts",
                           "mean_rts",
                           "median_rts",
                           "std_rts",
                           "skew_rts",
                           "kurt_rts",
                           "entropy_rts",
                           "min_tokens",
                           "max_tokens",
                           "mean_tokens",
                           "median_tokens",
                           "std_tokens",
                           "skew_tokens",
                           "kurt_tokens",
                           "entropy_tokens"]]

    sentiment_features = df[[
        "tweet_emoji_ratio",
        "most_common_emoji",
        "min_emoji_per_tweet",
        "max_emoji_per_tweet",
        "mean_emoji_per_tweet",
        "median_emoji_per_tweet",
        "std_emoji_per_tweet",
        "skew_emoji_per_tweet",
        "kurt_emoji_per_tweet",
        "entropy_emoji_per_tweet",
        "min_pos_emoji_per_tweet",
        "max_pos_emoji_per_tweet",
        "mean_pos_emoji_per_tweet",
        "median_pos_emoji_per_tweet",
        "std_pos_emoji_per_tweet",
        "skew_pos_emoji_per_tweet",
        "kurt_pos_emoji_per_tweet",
        "entropy_pos_emoji_per_tweet",
        "min_neg_emoji_per_tweet",
        "max_neg_emoji_per_tweet",
        "mean_neg_emoji_per_tweet",
        "median_neg_emoji_per_tweet",
        "std_neg_emoji_per_tweet",
        "skew_neg_emoji_per_tweet",
        "kurt_neg_emoji_per_tweet",
        "entropy_neg_emoji_per_tweet",
        "min_neu_emoji_per_tweet",
        "max_neu_emoji_per_tweet",
        "mean_neu_emoji_per_tweet",
        "median_neu_emoji_per_tweet",
        "std_neu_emoji_per_tweet",
        "skew_neu_emoji_per_tweet",
        "kurt_neu_emoji_per_tweet",
        "entropy_neu_emoji_per_tweet",
        "min_pos_sent_per_tweet",
        "max_pos_sent_per_tweet",
        "mean_pos_sent_per_tweet",
        "median_pos_sent_per_tweet",
        "std_pos_sent_per_tweet",
        "skew_pos_sent_per_tweet",
        "kurt_pos_sent_per_tweet",
        "entropy_pos_sent_per_tweet",
        "min_neg_sent_per_tweet",
        "max_neg_sent_per_tweet",
        "mean_neg_sent_per_tweet",
        "median_neg_sent_per_tweet",
        "std_neg_sent_per_tweet",
        "skew_neg_sent_per_tweet",
        "kurt_neg_sent_per_tweet",
        "entropy_neg_sent_per_tweet",
        "min_neu_sent_per_tweet",
        "max_neu_sent_per_tweet",
        "mean_neu_sent_per_tweet",
        "median_neu_sent_per_tweet",
        "std_neu_sent_per_tweet",
        "skew_neu_sent_per_tweet",
        "kurt_neu_sent_per_tweet",
        "entropy_neu_sent_per_tweet"]]

    hashtag_network_features = df[["density", "avg_clustering", "triangles", "volume", "mass", "min_weight",
                                   "max_max_weight", "mean_weight", "median_weight", "std_weight", "skew_weight",
                                   "kurt_weight", "entropy_weight"]]

    return user_features, temporal_features, content_features, sentiment_features, hashtag_network_features


# group_features_no_rts(df=pickle.load(open('../data/multi_class_data', 'rb')))
