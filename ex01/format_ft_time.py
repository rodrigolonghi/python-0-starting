import datetime

def main():
    epoch = datetime.datetime(1970, 1, 1)
    now = datetime.datetime.now()
    delta = now - epoch
    seconds = delta.total_seconds()

    formatted_seconds = f"{seconds:,.4f} or {seconds:.2e} in scientific notation"
    formatted_date = now.strftime("%b %d %Y")

    print(f"Seconds since January 1, 1970: {formatted_seconds}\n{formatted_date}")

if __name__ == "__main__":
    main()
