// Sample rewards data structure
const rewardsData = {
    basePoints: {
        smartphone: {
            points: 500,
            description: "Basic smartphones in working condition"
        },
        laptop: {
            points: 1000,
            description: "Laptops with basic functionality"
        },
        tablet: {
            points: 400,
            description: "Tablets in working condition"
        },
        desktop: {
            points: 800,
            description: "Desktop computers with basic components"
        },
        printer: {
            points: 300,
            description: "Standard printers"
        },
        monitor: {
            points: 400,
            description: "Computer monitors"
        },
        tv: {
            points: 600,
            description: "Television sets"
        },
        camera: {
            points: 300,
            description: "Digital cameras"
        },
        console: {
            points: 400,
            description: "Gaming consoles"
        }
    },
    
    multipliers: {
        condition: {
            excellent: {
                factor: 1.5,
                description: "Like new, fully functional"
            },
            good: {
                factor: 1.2,
                description: "Minor wear, fully functional"
            },
            fair: {
                factor: 1.0,
                description: "Visible wear, functional"
            },
            poor: {
                factor: 0.7,
                description: "Significant damage"
            },
            broken: {
                factor: 0.4,
                description: "Non-functional"
            }
        },
        
        age: {
            "0-1": {
                factor: 1.3,
                description: "Less than 1 year old"
            },
            "1-2": {
                factor: 1.1,
                description: "1-2 years old"
            },
            "2-3": {
                factor: 1.0,
                description: "2-3 years old"
            },
            "3-5": {
                factor: 0.8,
                description: "3-5 years old"
            },
            "5+": {
                factor: 0.6,
                description: "More than 5 years old"
            }
        },
        
        expiry: {
            shortTerm: {
                factor: 0.7,
                description: "Expected to expire within 6 months"
            },
            mediumTerm: {
                factor: 0.85,
                description: "Expected to expire within 12 months"
            },
            standardTerm: {
                factor: 1.0,
                description: "Expected to expire within 24 months"
            },
            longTerm: {
                factor: 1.2,
                description: "Expected to expire after 24 months"
            }
        }
    },
    
    premiumBrands: {
        apple: {
            factor: 1.2,
            description: "Apple products"
        },
        samsung: {
            factor: 1.2,
            description: "Samsung devices"
        },
        dell: {
            factor: 1.2,
            description: "Dell computers"
        },
        hp: {
            factor: 1.2,
            description: "HP devices"
        },
        sony: {
            factor: 1.2,
            description: "Sony electronics"
        }
    },
    
    rewardTiers: [
        {
            name: "Bronze",
            minPoints: 0,
            maxPoints: 1000,
            benefits: [
                "Basic recycling service",
                "Points tracking",
                "Monthly newsletter"
            ]
        },
        {
            name: "Silver",
            minPoints: 1001,
            maxPoints: 5000,
            benefits: [
                "Priority pickup service",
                "10% bonus points",
                "Quarterly e-waste report"
            ]
        },
        {
            name: "Gold",
            minPoints: 5001,
            maxPoints: 15000,
            benefits: [
                "Premium pickup service",
                "25% bonus points",
                "Monthly sustainability workshop access",
                "Exclusive recycling events"
            ]
        },
        {
            name: "Platinum",
            minPoints: 15001,
            maxPoints: Infinity,
            benefits: [
                "VIP pickup service",
                "50% bonus points",
                "Personal recycling consultant",
                "Custom recycling solutions",
                "Recognition in annual report"
            ]
        }
    ]
};
