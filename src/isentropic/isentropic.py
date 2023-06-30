class Isentropic:
    """Isentropic relation for ideal gas
    
    Reference: Crocco, L. (1958). One-dimensional treatment of steady gas dynamics. Fundamentals of gas dynamics, 64-349. Page 107
    """
    def __init__(self, gamma = 1.4):
        """Initialize isentropic relation

        Args:
            gamma (float, optional): heat capacity ratio. Defaults to 1.4 (air).
        """
        self.gamma = gamma
        self.gm1 = gamma - 1
        self.hgm1 = 0.5*(gamma - 1)
        
    def get_t_ratio(self, M):
        """T0 over T

        Args:
            M (float): Mach number

        Returns:
            float: T0 over T
        """
        return 1 + self.hgm1*M**2
    
    def get_p_ratio(self, M):
        """P0 over P

        Args:
            M (float): Mach number

        Returns:
            float: P0 over P
        """
        return self.get_t_ratio(M)**(self.gamma/self.gm1)
    
    def get_r_ratio(self, M):
        """rho0 over rho

        Args:
            M (float): Mach number

        Returns:
            float: rho0 over rho
        """
        return self.get_p_ratio(M)/self.get_t_ratio(M)