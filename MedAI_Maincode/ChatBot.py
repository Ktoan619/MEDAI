import gradio as gr
import os
import time
import openai
#print(openai.VERSION)
from openai import OpenAI

model = "gpt-3.5-turbo-1106"
#openai.api_key = "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"

os.environ["OPENAI_API_KEY"] = "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"

#openai_client = openai.OpenAI(api_key=get_openai_key())
openai_client = OpenAI()
openai_threads = openai_client.beta.threads
openai_assistants = openai_client.beta.assistants
def create_assistant():
  assistant = openai_assistants.create(
    name="Bác sĩ",
    instructions="Bạn là một trợ lý tư vấn về sức khỏe. Bạn sẽ giúp người dùng giải thích các vấn đề sức khỏe và đưa ra giải pháp.",
    tools=[],
    model=model,
  )

  return assistant

def ask_assistant(user_question, thread, assistant):
  # Pass in the user question into the existing thread
  openai_threads.messages.create(
    thread_id=thread.id,
    role="user",
    content=user_question,
  )
  #
  # Use runs to wait for the assistant response
  run = openai_threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id,
    instructions=f'Lưu ý rằng người dùng không có kiến thức về y học, đặc biệt là vấn đề sức khỏe nên hãy giải thích câu trả lời một cách chi tiết và đơn giản.Giới hạn là 300 tokens'
  )

  is_running = True
  while is_running:
    run_status = openai_threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
    is_running = run_status.status != "completed"
    time.sleep(1)

  return run

def assistant_response(thread, run):
  # Get the messages list from the thread
  # history
  messages = openai_threads.messages.list(thread_id=thread.id)
  # print(messages.data)
  # Get the last message for the current run
  last_message = [message for message in messages.data if message.run_id == run.id and message.role == "assistant"][-1]
  # If an assistant message is found, print it
  if last_message:
    response = f"[Bs.Hera]: {last_message.content[0].text.value}"
  else:
    response = f"[Bs.Hera]: Xin lỗi, Tôi không chắc rằng có thể trả lời câu hỏi đó. Bạn có thể hỏi một câu khác được không?"
  return response
assistant = create_assistant()
thread = openai_threads.create()

def gpt_response(message,history):

  user_question = message
  run = ask_assistant(user_question, thread, assistant)
  response = assistant_response(thread, run)
  return response
def create_chatbot_tab() :
  demo = gr.ChatInterface(fn=gpt_response, examples=["sùi mào gà", "đau bụng", "đau đầu", "mụn"], title="Bs.Hera",
                          description = "Trợ lý ảo - tư vấn sức khỏe", theme = "soft", submit_btn = "Gửi", retry_btn = "Thử lại",
                          undo_btn = "Quay lại", clear_btn = "Xóa toàn bộ", stop_btn = "Tạm dừng")
  #def launch_interface:
  return demo
