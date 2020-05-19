#1-تتيح لك قدرة التعامل مع المصفوفات بطريقة أفضل من ال Lists الموجودة تلقائيا كشكل من أشكال تراكيب البيانات في البايثون.
import numpy as np
#2-الهدف الأساسي لمكتبة Pandas هو إجراء ما يسمى ب Data Munging، ونقصد بهذا المصطلح إجراء تغييرات على بيانات أساسية غير مرتبة (Raw data) بحيث تقوم عملية التغيير هذه بتحويل البيانات إلى بيانات مفهومة ومفيدة.
import pandas as pd
#3-هي مختصة برسومات 2D، وعلى الرغم من أن هذه المكتبة من أقدم المكتبات المختصة بالإظهار المرئي للبيانات، إلا أنها ما زالت تتربع على عرش المكتبات المُستخدمة في هذا المجال، وتم بناؤها لتكون مُشابهة لدور برنامج Matlab.
import matplotlib.pyplot as plt
#4-can be used for data visualization. In this article we will look at Seaborn which is another extremely useful library for data visualization in Python. 
import seaborn as sns

data=pd.read_csv(r"D:\course  python\sample sheets\New folder\AB_NYC_2019.csv")
#عشان حجم الداتا كبيره بنستخدم الفانكشن عشان نقطع جزء من البيانات 
data.head(3)
#هنملي القيم الناقصه  بصفر مؤقتا 
#هنمسح الكود ده عشان هيسببلنا مشاكل بعد كده هيكون عندي اصفار كتير
#data.fillna(0,inplace=True)
y=data["price"]
#هنشيل الداتا الي عايزين نتوقعهاو عندنا هنا هتكون السعر
data=data.drop("price",axis=1)
x=data
#هنمسح الداتا الي ملهاش لازمه عندنا و هنا كانت 4 
x=x.drop("id",axis=1)
x=x.drop("host_id",axis=1)
x=x.drop("name",axis=1)
x=x.drop("host_name",axis=1)
#هنمسح خطوط الطول و العرض ملهاش لازمه بالنسبه للسعر
x=x.drop(["latitude","longitude"],axis=1)

#هنحول الاسامي بروكلن و منهاتن عباره عن 0و1 عشان نقدر نعمل تحليل
#هنجيب حاجه اسمها دامي فاليوز الي انا مش عارف معناها ايه بالظبطك
df_ngroup=pd.get_dummies(x["neighbourhood_group"])
# طلع حوار صايع فشخ هندنا في العمود ده 5 مناطق ف لفو الكمبيوتر ادي لكل واحد فيهم صيغ 
#من 1لحد 5 ممكن الكمبيوتر يعمل عمليات منطقيه عليهم مثلا 1 اصغر من 5 ةهكذا لذالك ادا المنطقه الموجوده في العمود 1 و بقيه المناطق اداهم صفر
#عايزين نربط الداتا ببعض هنستخدم فانكشن  اول مره نستخدمها من مكتبه panda 
#الفانكشن دي بتدمج الصفوف الي طلعت من الفانكشن الي قبلها مع بقيه الداتا
x=pd.concat([x,df_ngroup],axis=1)
#هنمسح الصف ده لانه ملهوش لازمه دلوقتي اتحول 0 و 1 خلاص
x=x.drop("neighbourhood_group",axis=1)
#هنبدا شغل علي العرف 
df_room=pd.get_dummies(x["room_type"])
#هنحول ل 0و1
x=pd.concat([x,df_room],axis=1)
#هنمسح الغرف عشان حولناها
x=x.drop("room_type",axis=1)
#هنعمل مع نوع الجار الي عملناه مع كل الي فات
#df_ni=pd.get_dummies(x["neighbourhood"])

#x=pd.concat([x,df_ni],axis=1)

x=x.drop("neighbourhood",axis=1)

#هنشيل الجيران عشان عددهم 221 نوع و هتصعب التحليل عليا جدا لذالك نفضل نشيلها
#هنشوف موجود كام ىشى في الداتا
x.isna().sum
#هنبدا نعوض الداتا الناقصه
#هنستخدم المتوسط لملء الداتا 
x["reviews_per_month"].fillna(x["reviews_per_month"].mean(),inplace=True)
#هيغير الداتا باقرب حاجه عندها

x["last_review"].fillna(method="ffill",inplace=True)

#همسح معاد اخر تقيم لعدم اهميه القصوي بس ممكن نستخدمهم عادي
x=x.drop("last_review",axis=1)
#هستدعي الملفات تاني عشان تبقي الداتا بيور و عشان الغي الاصفار و الوحايد الكتير الي ضفتهم 
data_new=pd.read_csv(r"D:\course  python\sample sheets\New folder\AB_NYC_2019.csv")
#هنحاول نطلع علاقات بين البيانات 
x2=sns.countplot(x="neighbourhood_group",data=data_new)
#هحط عنوان للداتا ككل
plt.title("popular_neighbourhood_group")
#هنحط  عنوان للx
plt.xlabel("neighbourhood_group")
#هنحط  عنوانy

plt.ylabel("count")
#هعرض الداتا بتاعتي
plt.show()
#هنحاول نطلع علاقات بين البيانات من نفس النوع 
###########هنا بنعمل كل ده عشان الرسمه سواء المحاور او اسم الرسمه و ما يخصها
#لازم لازم نعمل بيانات الرسمه عشان نقدر نطلع علاقات 
x1=sns.countplot(x="room_type",data=data_new)
#هحط عنوان للداتا ككل

plt.title("room type distribution")
#هنحط  عنوان للx

plt.xlabel("room type")
#هنحط  عنوانy

plt.ylabel("frequency")
#هعرض الداتا بتاعتي

plt.show()
#هنبدا نطلع علاقات بين الداتا ما بين كل داتا علي حده 
#حجم الرسمه بتاعتي
plt.figure(figsize=(10,10))
#hue  مشش فاهم قصده كويسالي في اخر الكود يعتبر الاساس
x1=sns.countplot(x="room_type",data=data_new,hue="neighbourhood_group")
# الموجودين عنديout liers بتحددلي 
#Xالاساس و Y الفرعي
sns.boxenplot(x="neighbourhood_group",y="price",data=data_new)
#بعد الرن هيطلع كل الي فوق out liers و الي تحت متصلين
#هنعمل داتا جديده نتخلص فيها من الداتا الزياده في السعر
data_price=data_new[data_new["price"]<=400]
#عايزين نعرض الداتا بس في شكل هيستوجرام
data_price.price.plot(kind="hist")
#علاقه جديده
# رينج الاسعار الاكثر تكرارا
#هتساعدني في حجات كتير جدا لانها ممثله بيانيا
sns.boxenplot(x="neighbourhood_group",y="price",data=data_price)
#هنعمل حاجه جديده
plt.figure(figsize=(10,7))
#هجيب نسبه اليفيو بالنسبه للغرف 3 انواع 
data_price.groupby(["room_type"]).count()["number_of_reviews"].plot(kind="bar",alpha=.6)

#هنعمله بالنسبه للمناطق
data_price.groupby(["neighbourhood_group"]).count()["number_of_reviews"].plot(kind="bar",alpha=.6)











