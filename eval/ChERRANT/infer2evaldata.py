import json

def extract_correct_text(predict_text):
    try:
        start_idx = predict_text.find('{\"correct_text\"')
        end_idx = predict_text.find('}', start_idx) + 1
        correct_text_dict = json.loads(predict_text[start_idx:end_idx])
        return correct_text_dict.get("correct_text", "")
    except:
        return ""

# ³õÊ¼»¯Á½¸öÁÐ±íÀ´·Ö±ð´æ´¢Ô¤²âºÍ´ð°¸µÄÎÄ±¾
predict_texts = []
gold_texts = []

# ¶ÁÈ¡jsonÎÄ¼þ²¢´¦ÀíÊý¾Ý
with open('test_data_2w.json_infer.jsonl', 'r', encoding='utf-8') as file:
    for line in file:
        item = json.loads(line)
        correct_text = extract_correct_text(item['predict_text'])
        if not correct_text:
            continue
        gold_texts.append((item['id'], item['asr_text'], item['gold_text']))
        #gold_texts.append(item['gold_text'])
        predict_texts.append((item['id'], item['asr_text'], correct_text))
        #predict_texts.append(correct_text)

# Ð´ÈëÔ¤²âÎÄ¼þ
with open('predict.txt', 'w', encoding='utf-8') as predict_file:
    for id, asr_text, predict_text in predict_texts:
    #for predict_text in predict_texts:
        predict_file.write(f"{id}\t{asr_text}\t{predict_text}\n")
        #predict_file.write(f"{predict_text}\n")

# Ð´Èë´ð°¸ÎÄ¼þ
with open('answer.txt', 'w', encoding='utf-8') as answer_file:
    for id, asr_text, gold_text in gold_texts:
    #for gold_text in gold_texts:
        answer_file.write(f"{id}\t{asr_text}\t{gold_text}\n")
        #answer_file.write(f"{gold_text}\n")

