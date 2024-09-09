import React from "react";
import { useNavigate } from "react-router-dom";
import { Heading, Button, ButtonGroup, Card, CardBody, CardFooter, Container, Divider, Image, Stack, Text, useColorModeValue, GridItem, Grid } from '@chakra-ui/react'

const Home = () => {
  const navigate = useNavigate();

  const cambiosChacoHandler = () => {
    navigate('/cambiosChaco');
  }

  const maxicambiosHandler = () => {
    navigate('/maxicambios');
  }
  return (
    <Container maxW="container.md" className="mt-3">
      <Grid templateColumns='repeat(2, 1fr)' gap={6}>
        <GridItem>

          <Card maxW='sm' bg={useColorModeValue("gray.200","black.200")}>
            <CardBody>
              <Image
                src='https://www.maxicambios.com.py/themes/default/assets/images/about-us-mobile.png'
                alt='Maxicambios'
                borderRadius='lg'
                bg={useColorModeValue("white","white")}
                px={"10px"}
              />
              <Stack mt='6' spacing='3'>
                <Heading size='md'>Maxicambios</Heading>
                <Text>
                  Maxicambios inició sus actividades en el mercado de cambios del Paraguay el 16 de mayo de 2003, bajo la razón social de MAXICAMBIOS S.A.              
                </Text>
              </Stack>
            </CardBody>
            <Divider />
            <CardFooter>
              <ButtonGroup spacing='2'>
                <Button variant='solid' colorScheme='blue' onClick={maxicambiosHandler}>
                  Visitar
                </Button>
              </ButtonGroup>
            </CardFooter>
          </Card>
        </GridItem>

        <GridItem>
          <Card maxW='sm' bg={useColorModeValue("gray.200","black.200")}>
            <CardBody>
              <Image
                src='https://www.cambioschaco.com.py/wp-content/themes/cambioschaco/images/logo.png'
                alt='Cambios chaco'
                borderRadius='lg'
                bg={useColorModeValue("white","white")}
                py='2rem'
              />
              <Stack mt='6' spacing='3'>
                <Heading size='md'>Cambios chaco</Heading>
                <Text>
                  Maxicambios inició sus actividades en el mercado de cambios del Paraguay el 16 de mayo de 2003, bajo la razón social de MAXICAMBIOS S.A.              
                </Text>
              </Stack>
            </CardBody>
            <Divider />
            <CardFooter>
              <ButtonGroup spacing='2'>
                <Button variant='solid' colorScheme='blue' onClick={cambiosChacoHandler}>
                  Visitar
                </Button>
              </ButtonGroup>
            </CardFooter>
          </Card>
        </GridItem>
      </Grid>
    </Container>
  );
};

export default Home;