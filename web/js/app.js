document.addEventListener("DOMContentLoaded", () => {
    document.querySelector(".ContactForm").addEventListener("submit", e => {
        e.preventDefault();
    
        let form = new FormData(e.target);
        
        fetch("/api/sendmail", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                msg: form.get('msg'),
                name: form.get('name'),
                email: form.get('email')
            })
        });

        return false;
    });
});
