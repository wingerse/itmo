function q = calculate_q_score(generated, real)

real = hdrread(real);
generated = hdrread(generated);

q = test(generated, real);

end