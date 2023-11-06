from aiogram import types
class user:
    def webAppButton(text : str ="Просмотр анкет", url:str ="https://dosugrostov.site/") -> types.ReplyKeyboardMarkup: #создание клавиатуры с webapp кнопкой
        """
        создание клавиатуры с webapp кнопкой
        """
        # keyboard = types.InlineKeyboardMarkup(row_width=1) #создаем клавиатуру
        #    https://moonlit-creponne-b17d15.netlify.app 
        webAppTest = types.WebAppInfo(url = url) #создаем webappinfo - формат хранения url
        # one_butt = types.InlineKeyboardButton(text="Просмотр анкет", web_app=webAppTest) #создаем кнопку типа webapp
        
        one_butt = types.KeyboardButton(text=text, web_app=webAppTest) #создаем кнопку типа webapp
    
        return one_butt #возвращаем клавиатуру
    
    
    buttons_user_user = [   [webAppButton()] ]
    keyboard_user_user = types.ReplyKeyboardMarkup(keyboard=buttons_user_user)

    def keyboard_user_admin(id:int) -> types.ReplyKeyboardMarkup:
        """
        функция создает ReplyKeyboardMarkup для админки чтобы можно было изменять анкету
        """
        urlPanel = f"https://dosugrostov.site/adminQuestionnairePage/{id}"
        print("ffff", urlPanel)
        buttons = [[user.webAppButton(text="test", url=urlPanel)], 
                          [types.KeyboardButton(text= "panel")]]
        return types.ReplyKeyboardMarkup(keyboard=buttons)
 

    str_start = ("Бот для просмотра анкет \n" 
            "От @Black_chat_Rostov \n\n" 
            "Админ @Moderatormes")
    str_edit_type_user = ("Ваш статус пользователя изменился, добавились новые возможности")