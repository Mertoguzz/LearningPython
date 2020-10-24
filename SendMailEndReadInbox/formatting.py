msg_remplate="""Hello {name},
Than yo for joining {website}.We are very
happy to have you with us.
"""

def format_msg(my_name="Mert",my_website="google.com.tr"):
  my_message=  msg_remplate.format(name=my_name,website=my_website)
  return my_message


  