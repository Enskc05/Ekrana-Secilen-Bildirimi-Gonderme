from plyer import notification

notification_title=input("Lütfen bir başlık giriniz: ")

notification_message=input("Lütfen bir mesaj giriniz: ")

notification.notify(
    title=notification_title,
    message=notification_message,
    app_icon= None,
    timeout=15,
    toast=False
)