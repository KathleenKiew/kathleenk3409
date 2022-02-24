#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask


# In[2]:


app= Flask(__name__)


# In[3]:


from flask import request, render_template


# In[4]:


from keras.models import load_model


# In[5]:


@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        income = request.form.get("income")
        age = request.form.get("age")
        loan = request.form.get("loan")
        print(income, age, loan)
        model=load_model("credit_model")
        pred=model.predict([[float(income),float(age),float(loan)]])
        s="The predicted default score is" + str(pred)
        return(render_template("index.html",result=s))
    else:
        return(render_template("index.html",result="Error"))


# In[ ]:


if __name__=="__main__":
    app.run()


# In[ ]:




