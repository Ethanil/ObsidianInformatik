---
aliases: 
---
# Sequenzkalkülregeln 

$$\begin{align}
\text{Name}& &\text{Left}& &\text{Right} \\
\\
not&         
&\frac{\Gamma \Rightarrow \Phi, \Delta}{\Gamma, \lnot \Phi \Rightarrow \Delta}&    
&\frac{\Gamma, \Phi \Rightarrow \Delta}{\Gamma \Rightarrow \lnot \ \Phi, \Delta}   \\   
\\
and&         
&\frac{\Gamma, \Psi, \Phi \Rightarrow \Delta}{\Gamma, \Psi \land \Phi \Rightarrow \Delta}&       
&\frac{\Gamma\Rightarrow \Psi,  \Delta \ \ \ \ \ \ \Gamma\Rightarrow \Phi,  \Delta }{\Gamma \Rightarrow  \Psi \land \Phi, \Delta}     \\ 
\\
or&         
&\frac{\Gamma, \Psi \Rightarrow \Delta \ \ \ \ \ \  \Gamma, \Phi \Rightarrow \Delta}{\Gamma, \Psi \lor \Phi \Rightarrow \Delta}&       
&\frac{\Gamma\Rightarrow \Psi,\Phi,\Delta}{\Gamma, \Psi \lor \Phi \Rightarrow \Delta}     \\ 
\\
impl&       
&\frac{\Gamma, \Psi \Rightarrow \Delta \ \ \ \ \ \  \Gamma \Rightarrow \Phi, \Delta }{\Gamma, \Phi \rightarrow \Psi \Rightarrow \Delta}&     
&\frac{\Gamma, \Phi  \Rightarrow \Psi, \Delta}{\Gamma\Rightarrow \Phi \rightarrow \Psi , \Delta}   \\    
\\
 \forall&  
 &\frac{\Gamma, \forall x;\Phi, [x/t']\Phi  \Rightarrow\Delta}{\Gamma, \forall x; \Phi \Rightarrow \Delta}&      
 &\frac{\Gamma \Rightarrow [x/c]\Phi, \Delta}{\Gamma, \Rightarrow \forall x; \Phi, \Delta}     \\
\\
 \exists&  
 &\frac{\Gamma, [x/c]\Phi \Rightarrow \Delta}{\Gamma, \exists x;\Phi \Rightarrow \Delta}&       
 &\frac{\Gamma \Rightarrow \exists x;\Phi,[x/t']\Phi \Delta}{\Gamma \Rightarrow \exists x;\Phi, \Delta}    \\
\\
 \doteq&   
 &\frac{\Gamma, t \doteq t' \Rightarrow [t/t']\Phi, \Delta}{\Gamma, t \doteq t' \Rightarrow \Phi, \Delta}&       
 &\frac{\Gamma,  t \doteq t', [t/t']\Phi \Rightarrow \Delta}{\Gamma,t\doteq t',\Phi \Rightarrow t   \Delta}    \\
\\
 equals& &\frac{}{\Gamma \Rightarrow t \doteq t,  \Delta}& &        \\
\\
 close& &\frac{}{\Gamma, \Phi \Rightarrow \Phi, \Delta}& & &   \\
\\
 true& &\frac{}{\Gamma \Rightarrow true, \Delta}& &  \\
\\
 false& &\frac{}{\Gamma, false \Rightarrow  \Delta}& &        \\
\end{align}$$


## Links