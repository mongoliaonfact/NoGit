



objective_function <- function(params) {
  alpha <- params[1]
  beta <- params[2]
  
  constraint1 <- abs(0.25 - pbeta(0.03, alpha, beta))
  constraint2 <- abs(0.75 - pbeta(0.15, alpha, beta))
  constraint3 <- abs(0.10 - (1 - pbeta(0.25, alpha, beta)))
  
  return(constraint1 + constraint2 + constraint3)
}

initial_params <- c(1, 1)
result <- optim(initial_params, objective_function, 
                method = "L-BFGS-B", lower = c(0, 0), upper = c(100, 100))
alpha_estimate <- result$par[1]
beta_estimate <- result$par[2]


cat("P(X < 0.03):", pbeta(0.03, alpha_estimate, beta_estimate), "\n")
cat("P(X < 0.15):", pbeta(0.15, alpha_estimate, beta_estimate), "\n")
cat("P(X > 0.25):", 1 - pbeta(0.25, alpha_estimate, beta_estimate), "\n")

# Estimated alpha and beta from the previous answer
alpha_estimate <- result$par[1]
beta_estimate <- result$par[2]

# Calculate the mean of the beta distribution
p <- alpha_estimate / (alpha_estimate + beta_estimate)

# Number of storms
n <- 25

# Calculate the probabilities for each possible number of overflows (0 to 25) using the binomial distribution
probabilities <- dbinom(0:n, size = n, prob = p)

# Print the probabilities
cat("Probability of river overflowing its banks in the next 25 storms:\n")
for (i in 0:n) {
  cat(sprintf("P(X = %d): %f\n", i, probabilities[i + 1]))
}
