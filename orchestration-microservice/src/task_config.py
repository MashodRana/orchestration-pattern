# task_config.py

class TaskNames:
    SPLIT_AUDIO = "split.tasks.split_audio"
    TRANSCRIBE_AUDIO = "transcription.tasks.transcribe_audio"
    DETECT_SENTIMENT = "nlp.tasks.detect_sentiment"


class Queues:
    SPLIT = "split_queue"
    TRANSCRIPTION = "transcription_queue"
    NLP = "nlp_queue"