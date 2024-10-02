import React from "react";
import { useNavigate } from "react-router-dom";
import { Heading, Button, ButtonGroup, Card, CardBody, CardFooter, Container, Divider, Image, Stack, Text, useColorModeValue, GridItem, Grid } from '@chakra-ui/react'

const Home = () => {
  const navigate = useNavigate();
  const imageBgColor = useColorModeValue("white","white");
  const cardBgColor = useColorModeValue("gray.200","black.200");
  const nvgtHandler = (e) => {
    navigate(`/${e.target.dataset.nvgtValue}`);
  }
  const casas = [
    {'head':'Maxicambios',
      'src':'https://www.maxicambios.com.py/themes/default/assets/images/about-us-mobile.png',
      'text':'Maxicambios inició sus actividades en el mercado de cambios del Paraguay el 16 de mayo de 2003, bajo la razón social de MAXICAMBIOS S.A.',
      'nvgt':'maxicambios'
    },
    {'head':'Cambios Chaco',
      'src':'https://www.cambioschaco.com.py/wp-content/themes/cambioschaco/images/logo.png',
      'text':'Cambios Chaco S.A. ha sido autorizada por Resolución N° 13, Acta N° 72 del 24 de Mayo de 1.989, del Banco Central del Paraguay.',
      'nvgt':'cambioschaco'
    },
    {'head':'Cambios Alberdi',
      'src':'https://www.cambiosalberdi.com/assets/img/logo/logo_menu-white.png',
      'text':'Mariscal Lopez Nro 4217 C/Capitan Dimas Motta - Asunción',
      'nvgt':'cambiosalberdi'
    },
//    {'head':'',
//      'src':'',
//      'text':'',
//      'nvgt':''
//    },
  ]
  return (
    <Container maxW="container.md" className="mt-3">
      <Grid templateColumns='repeat(2, 1fr)' gap={6}>
        {casas.map((casa)=>(
            <GridItem>
              <Card maxW='sm' bg={cardBgColor}>
                <CardBody>
                  <Image
                    src={casa.src}
                    alt={casa.head}
                    borderRadius='lg'
                    bg={imageBgColor}
                    px={"10px"}
                    py={"5rem"}
                    minH={"20rem"}
                  />
                  <Stack mt='6' spacing='3'>
                    <Heading size='md'>{casa.head}</Heading>
                    <Text>
                    {casa.text}              
                    </Text>
                  </Stack>
                </CardBody>
                <Divider />
                <CardFooter>
                  <ButtonGroup spacing='2'>
                    <Button variant='solid' colorScheme='blue' data-nvgt-value={casa.nvgt} onClick={nvgtHandler}>
                      Visitar
                    </Button>
                  </ButtonGroup>
                </CardFooter>
              </Card>
            </GridItem>
        ))}
      </Grid>
    </Container>
  );
};

export default Home;