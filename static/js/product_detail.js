// document.addEventListener("DOMContentLoaded", function () {

//     function initFlickity(selector, options) {
//         var element = document.querySelector(selector);

//         if (element) {
//             return new Flickity(element, options);
//         }
//     }
//     const defaultOptions = {
//         cellAlign: 'center',
//         wrapAround: true,
//         autoPlay: 4000,
//         prevNextButtons: true,
//         pageDots: true,
//         draggable: true,
//         contain: true
//     };

//     initFlickity('.featured-carousel', defaultOptions);

//     initFlickity('.dete-carousel', {
//         cellAlign: 'left',
//         wrapAround: true,
//         autoPlay: 5000,
//         prevNextButtons: false,
//         pageDots: true,
//         draggable: true,
//         adaptiveHeight: true
//     });
// });

document.addEventListener("DOMContentLoaded", function () {

    // ====== Image Zoom & Switch ======
    function changeMainImagePro(el){
        const mainImg = document.getElementById("mainImagePro");
        mainImg.src = el.src;
        document.querySelectorAll(".thumb-pro").forEach(t=>t.classList.remove("active-thumb"));
        el.classList.add("active-thumb");
    }
    window.changeMainImagePro = changeMainImagePro;

    // ====== Quantity Update ======
    function updateQtyPro(value){
        const input = document.getElementById("qtyPro");
        let newVal = parseInt(input.value) + value;
        if(newVal >= 1) input.value = newVal;
    }
    window.updateQtyPro = updateQtyPro;

    // ====== AJAX Add to Cart ======
    const addBtns = document.querySelectorAll(".btn-add-pro, #stickyAddPro");
    addBtns.forEach(btn=>{
        btn.addEventListener("click", async ()=>{
            const qty = parseInt(document.getElementById("qtyPro").value);
            try{
                const res = await fetch("{% url 'cart:add' product.id %}",{
                    method:"POST",
                    headers:{
                        "Content-Type":"application/json",
                        "X-CSRFToken":"{{ csrf_token }}"
                    },
                    body: JSON.stringify({quantity: qty})
                });
                if(!res.ok) throw new Error("خطأ في الإضافة");
                await res.json();
                showNotification("تمت إضافة المنتج للسلة ✅");
            }catch(err){
                console.error(err);
                showNotification("حدث خطأ أثناء الإضافة ❌");
            }
        });
    });

    // ====== Tabs ======
    document.querySelectorAll(".tab-menu-pro li").forEach(tab=>{
        tab.addEventListener("click", function(){
            document.querySelectorAll(".tab-menu-pro li").forEach(t=>t.classList.remove("active"));
            this.classList.add("active");
            const id = this.dataset.tab;
            document.querySelectorAll(".tab-item-pro").forEach(c=>c.classList.remove("active"));
            document.getElementById(id).classList.add("active");
        });
    });

    // ====== Notification ======
    function showNotification(msg){
        const notif = document.createElement("div");
        notif.className = "cart-notification";
        notif.innerText = msg;
        document.body.appendChild(notif);
        setTimeout(()=>notif.style.opacity = 1,50);
        setTimeout(()=>{notif.style.opacity=0; setTimeout(()=>notif.remove(),500)},2500);
    }

});