# ==========================================
# WhatsApp Group Chat Analyzer
# DADS Minor Project
# ==========================================

FILE_PATH = "C:/Users/shiha/OneDrive/Desktop/whatsapp analyzer/DADS_Minor_PROJECT_dataset.txt.txt"

STOPWORDS = {
    "the", "is", "and", "to", "a", "of", "in", "i", "you", "for",
    "on", "with", "was", "it", "that", "at", "this", "have", "we",
    "are", "be", "so", "if", "not", "do", "did", "your", "my", "me",
    "he", "she", "his", "her", "they", "them", "an", "as", "or",
    "but", "just", "guys", "yaar", "bhai", "hai", "na", "haan",
    "kya", "ja", "abhi", "abey"
}


# ==========================================
# Read Chat File
# ==========================================

def parse_chat(file_path):

    chats = []

    with open(file_path, "r", encoding="utf-8") as file:

        for line in file:

            line = line.strip()

            if " - " not in line:
                continue

            if ": " not in line:
                continue

            date_time, rest = line.split(" - ", 1)
            date, time = date_time.split(", ", 1)
            sender, message = rest.split(": ", 1)

            chats.append({
                "date": date,
                "hour": time[:2],
                "sender": sender,
                "message": message,
                "is_media": "<Media omitted>" in message
            })

    return chats


# ==========================================
# Messages Per User
# ==========================================

def messages_per_user(chats):

    counts = {}

    for chat in chats:

        sender = chat["sender"]

        if sender not in counts:
            counts[sender] = 0

        counts[sender] += 1

    return counts


# ==========================================
# Busiest Day
# ==========================================

def busiest_day(chats):

    days = {}

    for chat in chats:

        date = chat["date"]

        if date not in days:
            days[date] = 0

        days[date] += 1

    max_day = ""
    max_count = 0

    for day in days:

        if days[day] > max_count:
            max_day = day
            max_count = days[day]

    return max_day, max_count


# ==========================================
# Busiest Hour
# ==========================================

def busiest_hour(chats):

    hours = {}

    for chat in chats:

        hour = chat["hour"]

        if hour not in hours:
            hours[hour] = 0

        hours[hour] += 1

    max_hour = ""
    max_count = 0

    for hour in hours:

        if hours[hour] > max_count:
            max_hour = hour
            max_count = hours[hour]

    return max_hour, max_count


# ==========================================
# Average Message Length
# ==========================================

def average_message_length(chats):

    total_words = {}
    total_messages = {}

    for chat in chats:

        sender = chat["sender"]

        if sender not in total_words:
            total_words[sender] = 0
            total_messages[sender] = 0

        total_words[sender] += len(chat["message"].split())
        total_messages[sender] += 1

    averages = {}

    for sender in total_words:
        averages[sender] = round(
            total_words[sender] / total_messages[sender], 2)

    return averages


# ==========================================
# Media Messages
# ==========================================

def media_count_per_user(chats):

    media = {}

    for chat in chats:

        if chat["is_media"]:

            sender = chat["sender"]

            if sender not in media:
                media[sender] = 0

            media[sender] += 1

    return media


# ==========================================
# Top Words
# ==========================================

def top_words(chats):

    words = {}

    punctuation = ".,!?():;-\"'"

    for chat in chats:

        message = chat["message"].lower()

        for p in punctuation:
            message = message.replace(p, "")

        for word in message.split():

            if word in STOPWORDS:
                continue

            if word.isdigit():
                continue

            if word not in words:
                words[word] = 0

            words[word] += 1

    result = sorted(words.items(), key=lambda x: x[1], reverse=True)

    return result[:10]


# ==========================================
# Most Active User
# ==========================================

def most_active_user(counts):

    user = ""
    maximum = 0

    for name in counts:

        if counts[name] > maximum:
            maximum = counts[name]
            user = name

    return user, maximum


# ==========================================
# Print Report
# ==========================================

def print_report(chats):

    print("=" * 55)
    print("      WHATSAPP GROUP CHAT ANALYSIS REPORT")
    print("=" * 55)

    print("\nTotal Messages :", len(chats))

    user_counts = messages_per_user(chats)

    print("\nMessages Per User")
    print("-" * 30)

    for user in user_counts:
        print(user, ":", user_counts[user])

    user, count = most_active_user(user_counts)
    print("\nMost Active User :", user, "-", count)

    day, day_count = busiest_day(chats)
    print("Busiest Day :", day, "-", day_count)

    hour, hour_count = busiest_hour(chats)
    print("Busiest Hour :", hour + ":00", "-", hour_count)

    print("\nAverage Words Per Message")
    print("-" * 30)

    averages = average_message_length(chats)

    for user in averages:
        print(user, ":", averages[user])

    print("\nMedia Messages")
    print("-" * 30)

    media = media_count_per_user(chats)

    if len(media) == 0:
        print("No media messages.")
    else:
        for user in media:
            print(user, ":", media[user])

    print("\nTop 10 Words")
    print("-" * 30)

    words = top_words(chats)

    rank = 1

    for word, count in words:
        print(rank, ".", word, "-", count)
        rank += 1

    print("\n" + "=" * 55)
    print("END OF REPORT")
    print("=" * 55)


# ==========================================
# Main Program
# ==========================================

if __name__ == "__main__":

    chat_data = parse_chat(FILE_PATH)

    print_report(chat_data)