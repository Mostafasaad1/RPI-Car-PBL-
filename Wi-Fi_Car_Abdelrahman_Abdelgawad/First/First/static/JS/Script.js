        /* <<<< Toggle Switch ...... */
        const toggle = document.getElementById('toggle');
        toggle.onclick = function(){
        toggle.classList.toggle('active')
        }
        /* ................................ >>>> */
        /* <<<< Keyboard Linking with Buttons ...... */
        let keys = document.querySelectorAll('.keys');
        //console.log(keys);
        for(let i = 0; i < keys.length; i++) {
            keys[i].setAttribute('keyname', keys[i].innerText);
            keys[i].setAttribute('lowerCaseName', keys[i].innerText.toLowerCase());
        }
        window.addEventListener('keydown', function(e) {
            for(let i = 0; i < keys.length; i++) {
                if(e.key == keys[i].getAttribute('keyname' ) || e.key == keys[i].getAttribute('lowerCaseName')) {
                    keys[i].classList.add('active')
                }
            }
        })
        window.addEventListener('keyup', function(e) {
            for(let i = 0; i < keys.length; i++) {
                if(e.key == keys[i].getAttribute('keyname' ) || e.key == keys[i].getAttribute('lowerCaseName')) {
                    keys[i].classList.remove('active')
                    keys[i].classList.add('remove')
                }
                setTimeout(()=> {
                    keys[i].classList.remove('remove')
                },200)
            }
        })
        /* ................................ >>>> */
