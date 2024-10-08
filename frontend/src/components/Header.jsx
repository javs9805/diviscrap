import {
  Box,
  Flex,
  Button,
  useColorModeValue,
  Stack,
  useColorMode,
  Container,
} from '@chakra-ui/react'
import { MoonIcon, SunIcon } from '@chakra-ui/icons'

const Header = () => {
  const { colorMode, toggleColorMode } = useColorMode()
  const homeRedHandler = () => {
    window.location.href = '/';
  };
  return (
    <>
      <Box bg={useColorModeValue('gray.100', 'gray.900')} px={4} mb={3}>
        <Container maxW="container.md">
          <Flex h={16} alignItems={'center'} justifyContent={'space-between'}>
            <Box><Button onClick={homeRedHandler}>{'<Diviscrap />'}</Button></Box>

            <Flex alignItems={'center'}>
              <Stack direction={'row'} spacing={7}>
                <Button onClick={toggleColorMode}>
                  {colorMode === 'light' ? <MoonIcon /> : <SunIcon />}
                </Button>
              </Stack>
            </Flex>
          </Flex>
        </Container>
      </Box>
    </>
  )
}

export default Header;