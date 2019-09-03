#include <math.h>
#include <stdlib.h>
#include <stdio.h>
#include <R.h>
//need to figure out how to import the R library and math and everything else

int stone(double *z, double *v,double *aU, double *aL,
          double *s,double *h,double *resp,double *rt,double *n,double *maxiter,double *nDotsVector)
{
    //   double t,rhs,x,hv,samplev;
    double rhs,x;
    int N,i,iter,Maxiter,nDots;
    
    /* Convert some double inputs to integer types. */
    N=(int) *n;
    Maxiter =(int) *maxiter;
    GetRNGstate();  //VK seems to be are R random function? Not sure
    rhs=sqrt(*h)*(*s);
    for (i=0;i<N;i++) {
        x=*z;
        iter=0;
        resp[i]=(double) -1.0 ;
        do
        {
            nDots = nDotsVector[iter];
            iter = iter+1;
            x = x+(*h)*((*v)*(nDots))+rhs*norm_rand();
            if (x>=*aU) {
                resp[i]=(double) 1.0 ;
                break ;
            }
            if (x<=*aL)
            resp[i]=(double) 2.0 ;
            break ;
        }
    } while (iter<Maxiter) ;
    rt[i]=((double) iter)*(*h) - (*h)/((double) 2.0);
}
PutRNGstate(); //putting out the random state
}




int stoneUGM(double *z, double *v,double *aU, double *aL, double *timecons, double *usign,
             double *s,double *h,double *resp,double *rt,double *n,double *maxiter,double *nDotsVector)
{
    //   double t,rhs,x,hv,samplev;
    double rhs,x,alpha,xu;   // xu stores x + urgency signal at each time point
    int N,i,iter,Maxiter,nDots;
    //do I need to do any conversions in python ?mutlipl
    /* Convert some double inputs to integer types. */
    N=(int) *n;
    Maxiter =(int) *maxiter;
    GetRNGstate();
    rhs=sqrt(*h)*(*s);
    // weight for exponentially-weighted moving average
    // alpha=(*h)/((*h)+(*timecons));
    alpha=(*timecons)/((*timecons)+(*h));
    for (i=0;i<N;i++) {
        x=*z;
        iter=0;
        resp[i]=(double) -1.0 ;
        do
        {
            nDots = nDotsVector[iter];
            iter = iter+1;
            //       x = x+(*h)*(*v)+rhs*norm_rand();   // Stone model
            // filtered signal from previous step + input from current step
            x = alpha*x + (1-alpha)*((*h)*((*v)*(nDots)) + rhs*norm_rand());
            // multiply linear urgency signal. usign determines size of urgency signal
            //xu = x * iter*(*h)*(*usign);  // urgency is multiplicative
            xu = x * iter*(*usign);  // urgency is multiplicative
            if (xu>=*aU) {
                resp[i]=(double) 1.0 ;
                break ;
            }
            if (xu<=*aL) {
                resp[i]=(double) 2.0 ;
                break ;
            }
        } while (iter<Maxiter) ;
        rt[i]=((double) iter)*(*h) - (*h)/((double) 2.0);
    }
    PutRNGstate();
}





int stoneEta(double *z, double *v, double *eta, double *aU, double *aL,
             double *s,double *h,double *resp,double *rt,double *n,double *maxiter,double *nDotsVector)
{
    //   double t,rhs,x,hv,samplev;
    double rhs,x,samplev;
    int N,i,iter,Maxiter,nDots;
    
    /* Convert some double inputs to integer types. */
    N=(int) *n;
    Maxiter =(int) *maxiter;
    GetRNGstate();
    rhs=sqrt(*h)*(*s);
    for (i=0;i<N;i++) {
        samplev=(*v)+(*eta)*norm_rand();
        x=*z;
        iter=0;
        resp[i]=(double) -1.0 ;
        do
        {
            nDots = nDotsVector[iter];
            iter = iter+1;
            //       x = x+(*h)*(*v)+rhs*norm_rand();
            x = x+(*h)*((samplev)*(nDots))+rhs*norm_rand();
            if (x>=*aU) {
                resp[i]=(double) 1.0 ;
                break ;
            }
            if (x<=*aL) {
                resp[i]=(double) 2.0 ;
                break ;
            }
        } while (iter<Maxiter) ;
        rt[i]=((double) iter)*(*h) - (*h)/((double) 2.0);
    }
    PutRNGstate();
}


int stoneEtaUGM(double *z, double *v,double *eta, double *aU, double *aL, double *timecons,
                double *usign, double *s,double *h,double *resp,double *rt,double *n,double *maxiter,double *nDotsVector)
{
    //   double t,rhs,x,hv,samplev;
    double rhs,x,alpha,xu,samplev;   // xu stores x + urgency signal at each time point
    int N,i,iter,Maxiter,nDots;
    
    /* Convert some double inputs to integer types. */
    N=(int) *n;
    Maxiter =(int) *maxiter;
    GetRNGstate();
    rhs=sqrt(*h)*(*s);
    // weight for exponentially-weighted moving average
    // alpha=(*h)/((*h)+(*timecons));
    alpha=(*timecons)/((*timecons)+(*h));
    for (i=0;i<N;i++) {
        samplev=(*v)+(*eta)*norm_rand();
        x=*z;
        iter=0;
        resp[i]=(double) -1.0 ;
        do
        {
            nDots = nDotsVector[iter];
            iter = iter+1;
            //       x = x+(*h)*(*v)+rhs*norm_rand();   // Stone model
            // filtered signal from previous step + input from current step
            //       x = alpha*x + (1-alpha)*((*h)*(*v) + rhs*norm_rand());
            x = alpha*x + (1-alpha)*((*h)*((samplev)*(nDots)) + rhs*norm_rand());
            // multiply linear urgency signal. usign determines size of urgency signal (1 in Cisek, 2 in Thura)
            //xu = x * iter*(*h)*(*usign);  // urgency is multiplicative
            xu = x * iter*(*usign);  // urgency is multiplicative
            if (xu>=*aU) {
                resp[i]=(double) 1.0 ;
                break ;
            }
            if (xu<=*aL) {
                resp[i]=(double) 2.0 ;
                break ;
            }
        } while (iter<Maxiter) ;
        rt[i]=((double) iter)*(*h) - (*h)/((double) 2.0);
    }
    PutRNGstate();
}





int ratcliff(double *zmin, double *zmax, double *v,double *aU, double *aL, double *eta,
             double *s,double *h,double *resp,double *rt,double *n,double *maxiter,double *nDotsVector)
{
    double rhs,x,samplev;
    int N,i,iter,Maxiter,nDots;
    
    /* Convert some double inputs to integer types. */
    N=(int) *n;
    Maxiter =(int) *maxiter;
    GetRNGstate();
    rhs=sqrt(*h)*(*s);
    for (i=0;i<N;i++) {
        samplev=(*v)+(*eta)*norm_rand();
        x=*zmin + (*zmax-*zmin)*unif_rand();
        iter=0;
        resp[i]=(double) -1.0 ;
        do
        {
            nDots = nDotsVector[iter];
            iter = iter+1;
            x = x+(*h)*((samplev)*(nDots))+rhs*norm_rand();
            if (x>=*aU) {
                resp[i]=(double) 1.0 ;
                break ;
            }
            if (x<=*aL) {
                resp[i]=(double) 2.0 ;
                break ;
            }
        } while (iter<Maxiter) ;
        rt[i]=((double) iter)*(*h) - (*h)/((double) 2.0);
    }
    PutRNGstate();
}





int ratcliffUGM(double *zmin, double *zmax, double *v,double *aU, double *aL, double *eta,
                double *timecons, double *usign,
                double *s,double *h,double *resp,double *rt,double *n,double *maxiter,double *nDotsVector)
{
    double rhs,x,samplev,xu;
    int N,i,iter,Maxiter,nDots;
    
    /* Convert some double inputs to integer types. */
    N=(int) *n;
    Maxiter =(int) *maxiter;
    GetRNGstate();
    rhs=sqrt(*h)*(*s);
    for (i=0;i<N;i++) {
        samplev=(*v)+(*eta)*norm_rand();
        x=*zmin + (*zmax-*zmin)*unif_rand();
        iter=0;
        resp[i]=(double) -1.0 ;
        do
        {
            nDots = nDotsVector[iter];
            iter = iter+1;
            x = x+(*h)*((samplev)*(nDots))+rhs*norm_rand();
            // multiply linear urgency signal. usign determines size of urgency signal (1 in Cisek, 2 in Thura)
            //xu = x * iter*(*h)*(*usign);  // urgency is multiplicative
            xu = x * iter*(*usign);  // urgency is multiplicative
            if (xu>=*aU) {
                resp[i]=(double) 1.0 ;
                break ;
            }
            if (xu<=*aL) {
                resp[i]=(double) 2.0 ;
                break ;
            }
        } while (iter<Maxiter) ;
        rt[i]=((double) iter)*(*h) - (*h)/((double) 2.0);
    }
    PutRNGstate();
}
