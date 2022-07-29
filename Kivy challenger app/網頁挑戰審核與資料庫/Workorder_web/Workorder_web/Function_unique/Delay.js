function sleep(milliseconds) {
            var start = new Date().getTime();
            while (1)
                if ((new Date().getTime() - start) > milliseconds)
                    break;
        }