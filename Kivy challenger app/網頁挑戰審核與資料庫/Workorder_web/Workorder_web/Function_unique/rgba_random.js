function rgba_random(a) 
{
            var r = Math.floor(Math.random() * 256);
            var g = Math.floor(Math.random() * 256);
            var b = Math.floor(Math.random() * 256);
            var rgba = 'rgba(' + r + ',' + g + ',' + b + ',' + a + ')';
            return rgba;
}