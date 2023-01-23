FROM python:slim
ENV TOKEN='5716870555:AAGtImIXqHgJiC894CQThMm7niEhhymBBrc'
COPY . .
RUN pip install -r req.txt
CMD python bot.py