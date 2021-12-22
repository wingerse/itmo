function q = test(generated, real)
res = hdrvdp3( 'quality', generated, real, 'rgb-native', 30, {} );
q = res.Q;

end