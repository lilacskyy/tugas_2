Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
CSRF tersendiri merupakan serangan dalam web yang tersimple namun tetap memberi efek yang cukup parah. Serangan CSRF sudah terkenal muncul dari dahulu. Sedangkan Dengan adanya CSRF token, kita dapat melakukan pencegahan atas serangan CRSF sehingga orang yang ingin menyerang tidak dapat membuat permintaan HTTP yang betul-betul valid. Dengan penyerang tidaj tahu token CSRF user, maka penyerang tidak bisa melakukan permintaan dengan seluruh parameter yang dibutuhkan aplikasi untuk memenuhi permintaan tersebut. Oleh karena itu apabila tidak ada potongan kode csrf token itu pada elemen <form> adalah agar  