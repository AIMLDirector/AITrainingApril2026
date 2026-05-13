# from transformers import AutoModelForCausalLM, AutoTokenizer, Pipeline

# model = AutoModelForCausalLM.from_pretrained("bert-base-uncased", dtype="auto", device_map="auto")
# tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

# pipeline = Pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
# pipeline(" i am not liking the product from  honda")


from transformers import pipeline

classifier = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

result = classifier("i feel the customer support from maruti is very good and i am loving the product from maruti")

print(result)